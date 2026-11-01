---
records:
    - id: 9FP6QPTC5W
      kind: monograph
      title: Theoretical Numerical Analysis
      creators:
        - name: Kendall Atkinson
          role: author
        - name: Weimin Han
          role: author
      date: "2001"
      msc:
        - code: 65-01
          from: zbmath_search
        - code: 65N12
          from: zbmath_search
        - code: 46N40
          from: zbmath_search
        - code: 47N40
          from: zbmath_search
        - code: 65D05
          from: zbmath_search
        - code: 65Jxx
          from: zbmath_search
        - code: 65R20
          from: zbmath_search
        - code: 65L60
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi:
                - 10.1007/978-0-387-21526-6
                - 10.1007/978-0-387-28769-0
            zbl: "0966.65001"
            zbl_id: "1590936"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781468493016"
                    - "9780387215266"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2005"
              ids:
                isbn:
                    - "9780387258874"
                    - "9780387287690"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21526-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-28769-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1590936"
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
