---
records:
    - id: JKQE8RTGPH
      kind: monograph
      title: The Art of Random Walks
      creators:
        - name: András Telcs
          role: author
      date: "2006"
      msc:
        - code: 60-02
          from: zbmath_search
        - code: 60J10
          from: zbmath_search
        - code: 60J45
          from: zbmath_search
        - code: 31-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2006"
          ids:
            doi: 10.1007/b134090
            zbl: "1104.60003"
            zbl_id: "5038606"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2006"
              ids:
                isbn:
                    - "9783540330271"
                    - "9783540330288"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b134090
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5038606"
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
