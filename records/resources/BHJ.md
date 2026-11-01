---
records:
    - id: BHJGXKV7MF
      kind: monograph
      title: Linear Algebra
      creators:
        - name: Charles W. Curtis
          role: author
      date: "1984"
      expressions:
        - key: e1
          kind: edition
          date: "1984"
          ids:
            doi: 10.1007/978-1-4612-1136-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1984"
              ids:
                isbn:
                    - "9781461270195"
                    - "9781461211365"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1136-5
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: BHJKVT84X1
      kind: monograph
      title: 'Nonlinear Hyperbolic Problems: Proceedings of an Advanced Research Workshop held in St. Etienne, France January 13–17, 1986'
      creators:
        - name: Claude Carasso
          role: editor
        - name: Denis Serre
          role: editor
        - name: Pierre-Arnaud Raviart
          role: editor
      date: "1987"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1987"
          ids:
            doi:
                - 10.1007/bfb0078312
                - 10.1007/bfb0083863
            zbl: "0623.00008"
            zbl_id: "4010413"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540182009"
                    - "9783540478058"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1989"
              ids:
                isbn:
                    - "9783540517467"
                    - "9783540468004"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0078312
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0083863
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "4010413"
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
