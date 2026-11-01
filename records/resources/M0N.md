---
records:
    - id: M0N60SDVDY
      kind: monograph
      title: Versicherungsmathematik
      creators:
        - name: Walter Saxer
          role: author
      date: "1958"
      expressions:
        - key: e1
          kind: edition
          date: "1958"
          ids:
            doi: 10.1007/978-3-642-88631-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1958"
              ids:
                isbn:
                    - "9783642886324"
                    - "9783642886317"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-88631-7
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: M0NRWF3ZSM
      kind: monograph
      title: 'Algebraic Topology Barcelona 1986: Proceedings of a Symposium held in Barcelona, April 2–8, 1986'
      creators:
        - name: J. Aguadé
          role: editor
        - name: R. Kane
          role: editor
      date: "1987"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 55-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1987"
          ids:
            doi: 10.1007/bfb0082996
            zbl: "0626.00023"
            zbl_id: "4016800"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540187295"
                    - "9783540481225"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0082996
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "4016800"
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
