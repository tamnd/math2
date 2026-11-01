---
records:
    - id: 2RH8J5K35V
      kind: monograph
      title: 'Cohomologie Galoisienne: Cours au Collège de France, 1962–1963'
      creators:
        - name: Jean-Pierre Serre
          role: author
      date: "1965"
      msc:
        - code: 12G05
          from: zbmath_search
        - code: 12-02
          from: zbmath_search
        - code: 11R34
          from: zbmath_search
        - code: 20J05
          from: zbmath_search
        - code: "20E18"
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: fr
          date: "1965"
          ids:
            doi:
                - 10.1007/978-3-662-21553-1
                - 10.1007/978-3-662-21576-0
                - 10.1007/bfb0108758
            zbl: "0128.26303"
            zbl_id: "3209245"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1973"
              ids:
                isbn:
                    - "9783540060840"
                    - "9783662215531"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1965"
              ids:
                isbn:
                    - "9783540033493"
                    - "9783662215760"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783540580027"
                    - "9783540249276"
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
          native_id: 10.1007/978-3-662-21553-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-21576-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0108758
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3209245"
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
