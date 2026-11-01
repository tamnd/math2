---
records:
    - id: QMHTZYNGG7
      kind: monograph
      title: Global Differential Geometry and Global Analysis
      creators:
        - name: Dirk Ferus
          role: editor
        - name: Ulrich Pinkall
          role: editor
        - name: Udo Simon
          role: editor
        - name: Berd Wegner
          role: editor
      date: "1981"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 53-06
          from: zbmath_search
        - code: 58-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1981"
          ids:
            doi:
                - 10.1007/bfb0083621
                - 10.1007/bfb0088835
            zbl: "0437.00004"
            zbl_id: "3681682"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1991"
              ids:
                isbn:
                    - "9783540547280"
                    - "9783540464457"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1981"
              ids:
                isbn:
                    - "9783540102854"
                    - "9783540384199"
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
          native_id: 10.1007/bfb0083621
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0088835
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3681682"
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
