---
records:
    - id: H7T15S7ZSX
      kind: monograph
      title: Séminaire de Théorie du Potentiel Paris, No. 4
      creators:
        - name: Francis Hirsch
          role: editor
        - name: Gabriel Mokobodzki
          role: editor
      date: "1979"
      msc:
        - code: 00-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi: 10.1007/bfb0071316
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1979"
              ids:
                isbn:
                    - "9783540092520"
                    - "9783540353089"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0071316
          level: work
      history:
        - op: add
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
        - op: split
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
          note: split from V4D2YVABVV
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: to in
    - id: H7TQACY160
      kind: monograph
      title: Introduction to Noncommutative Algebra
      creators:
        - name: Matej Brešar
          role: author
      date: "2014"
      msc:
        - code: 16-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2014"
          ids:
            doi:
                - 10.1007/978-3-031-96296-7
                - 10.1007/978-3-319-08693-4
            zbl: "1334.16001"
            zbl_id: "6323220"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2025"
              ids:
                isbn:
                    - "9783031962950"
                    - "9783031962967"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2014"
              ids:
                isbn:
                    - "9783319086927"
                    - "9783319086934"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-96296-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-08693-4
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6323220"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
