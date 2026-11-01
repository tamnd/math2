---
records:
    - id: 6ZPTNZ2DFN
      kind: monograph
      title: 'Stochastic Processes — Mathematics and Physics II: Proceedings of the 2nd BiBoS Symposium held in Bielefeld, West Germany, April 15–19, 1985'
      creators:
        - name: Sergio Albeverio
          role: editor
        - name: Philippe Blanchard
          role: editor
        - name: Ludwig Streit
          role: editor
      date: "1986"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 60-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1986"
          ids:
            doi:
                - 10.1007/bfb0077343
                - 10.1007/bfb0080206
            zbl: "0572.00014"
            zbl_id: "3912302"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540177975"
                    - "9783540478355"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1986"
              ids:
                isbn:
                    - "9783540159988"
                    - "9783540397038"
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
          native_id: 10.1007/bfb0077343
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0080206
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3912302"
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
